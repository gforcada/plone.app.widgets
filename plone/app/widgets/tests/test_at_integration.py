# -*- coding: utf-8 -*-

try:
    import unittest2 as unittest
except ImportError:  # pragma: nocover
    import unittest  # pragma: nocover
    assert unittest  # pragma: nocover

from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.widgets.testing import PLONEAPPWIDGETS_INTEGRATION_TESTING
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName


class BaseWidgetTests(unittest.TestCase):
    """Tests for plone.app.widgets.at.BaseWidget
    """

    layer = PLONEAPPWIDGETS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']

        languages = getToolByName(self.portal, 'portal_languages')
        languages.manage_setLanguageSettings(
            'de', ['de'], setUseCombinedLanguageCodes=False)
        languages.setLanguageBindings()

        setRoles(self.portal, TEST_USER_ID, ['Manager'])

        self.example = self.portal[self.portal.invokeFactory(
            'ExampleType', id='example', title='Example')]

        class View(BrowserView):
            template = ViewPageTemplateFile('test_at_integration.pt')

            def render(self, **kw):
                return self.template(**kw)

        self.view = View(self.example, self.request)

    def tearDown(self):
        self.portal.manage_delObjects([self.example.getId()])

    def test_textinput(self):
        from plone.app.widgets.at import InputWidget
        field = self.example.getField('inputfield')
        self.assertIsInstance(field.widget, InputWidget)
        self.assertIn(
            '<input name="inputfield" type="text" value=""/>',
            self.view.render(field=field, mode='edit'))

    def test_date(self):
        from plone.app.widgets.at import DateWidget
        field = self.example.getField('datefield')
        self.assertIsInstance(field.widget, DateWidget)
        self.assertIn(
            '<input class="pat-pickadate" name="datefield" data-pat-pickadate="{&quot;pickadate-clear&quot;: &quot;Clear&quot;, &quot;pickadate-weekdaysFull&quot;: [&quot;Montag&quot;, &quot;Dienstag&quot;, &quot;Mittwoch&quot;, &quot;Donnerstag&quot;, &quot;Freitag&quot;, &quot;Samstag&quot;, &quot;Sonntag&quot;], &quot;format&quot;: &quot;yyyy-mm-dd @&quot;, &quot;pickadate-today&quot;: &quot;Today&quot;, &quot;pickadate-monthsShort&quot;: [&quot;Jan&quot;, &quot;Feb&quot;, &quot;Mrz&quot;, &quot;Apr&quot;, &quot;Mai&quot;, &quot;Jun&quot;, &quot;Jul&quot;, &quot;Aug&quot;, &quot;Sep&quot;, &quot;Okt&quot;, &quot;Nov&quot;, &quot;Dez&quot;], &quot;formatSubmit&quot;: &quot;yyyy-mm-dd&quot;, &quot;pickadate-weekdaysShort&quot;: [&quot;Mo&quot;, &quot;Di&quot;, &quot;Mi&quot;, &quot;Do&quot;, &quot;Fr&quot;, &quot;Sa&quot;, &quot;So&quot;], &quot;pickadate-monthsFull&quot;: [&quot;Januar&quot;, &quot;Februar&quot;, &quot;M\\u00e4rz&quot;, &quot;April&quot;, &quot;Mai&quot;, &quot;Juni&quot;, &quot;Juli&quot;, &quot;August&quot;, &quot;September&quot;, &quot;Oktober&quot;, &quot;November&quot;, &quot;Dezember&quot;]}" type="date" value="',  # noqa
            self.view.render(field=field, mode='edit'))

    def test_datetime(self):
        from plone.app.widgets.at import DatetimeWidget
        field = self.example.getField('datetimefield')
        self.assertIsInstance(field.widget, DatetimeWidget)
        self.assertIn(
            '<input class="pat-pickadate" name="datetimefield" data-pat-pickadate="{&quot;pickadate-clear&quot;: &quot;Clear&quot;, &quot;pickadate-weekdaysFull&quot;: [&quot;Montag&quot;, &quot;Dienstag&quot;, &quot;Mittwoch&quot;, &quot;Donnerstag&quot;, &quot;Freitag&quot;, &quot;Samstag&quot;, &quot;Sonntag&quot;], &quot;format&quot;: &quot;yyyy-mm-dd @ HH:MM&quot;, &quot;pickadate-today&quot;: &quot;Today&quot;, &quot;pickadate-monthsShort&quot;: [&quot;Jan&quot;, &quot;Feb&quot;, &quot;Mrz&quot;, &quot;Apr&quot;, &quot;Mai&quot;, &quot;Jun&quot;, &quot;Jul&quot;, &quot;Aug&quot;, &quot;Sep&quot;, &quot;Okt&quot;, &quot;Nov&quot;, &quot;Dez&quot;], &quot;formatSubmit&quot;: &quot;yyyy-mm-dd&quot;, &quot;pickadate-weekdaysShort&quot;: [&quot;Mo&quot;, &quot;Di&quot;, &quot;Mi&quot;, &quot;Do&quot;, &quot;Fr&quot;, &quot;Sa&quot;, &quot;So&quot;], &quot;pickadate-monthsFull&quot;: [&quot;Januar&quot;, &quot;Februar&quot;, &quot;M\\u00e4rz&quot;, &quot;April&quot;, &quot;Mai&quot;, &quot;Juni&quot;, &quot;Juli&quot;, &quot;August&quot;, &quot;September&quot;, &quot;Oktober&quot;, &quot;November&quot;, &quot;Dezember&quot;]}" type="datetime-local" value="',  # noqa
            self.view.render(field=field, mode='edit'))

    def test_select(self):
        from plone.app.widgets.at import SelectWidget
        field = self.example.getField('selectfield')
        self.assertIsInstance(field.widget, SelectWidget)
        self.assertIn(
            '<select name="selectfield"> </select>',
            self.view.render(field=field, mode='edit'))

    def test_select2(self):
        from plone.app.widgets.at import Select2Widget
        field = self.example.getField('select2field')
        self.assertIsInstance(field.widget, Select2Widget)
        self.assertIn(
            '<input class="pat-select2" name="select2field" data-pat-select2="{&quot;separator&quot;: &quot;;&quot;}" type="text" value=""/>',  # noqa
            self.view.render(field=field, mode='edit'))
