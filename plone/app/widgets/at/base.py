from Products.Archetypes.Widget import TypesWidget
from plone.app.widgets.base import BasePatternsWidget


class PatternsWidget(TypesWidget):
    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro': "patterns_widgets",
    })

    pattern_widget_klass = BasePatternsWidget
    pattern_el_type = 'input'

    @property
    def pattern_name(self):
        raise NotImplementedError('pattern_name not implemented!')

    def view(self, context, field, request):
        return field.getAccessor(context)()

    def edit(self, context, field, request):
        widget = self.pattern_widget_klass(self.pattern_name,
                                           self.pattern_el_type)
        widget.el.attrib['name'] = field.getName()

        value = request.get(field.getName(), field.getAccessor(context)())
        if value is None:
            value = ''

        if hasattr(self, 'customize_widget'):
            self.customize_widget(widget, value, context, field, request)

        return widget.render()
