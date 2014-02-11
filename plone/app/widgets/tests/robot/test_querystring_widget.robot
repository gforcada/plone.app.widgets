*** Settings ***

Resource  common.robot

Test Setup  Open SauceLabs test browser
Test Teardown  Run keywords  Report test status  Close all browsers

*** Variables ***
${querywidget_selector}  \#formfield-form-widgets-ICollection-query

*** Test Cases ***

Querystring Widget is working
  Given I'm logged in as a 'Site Administrator'
    And I create a collection  My Collection
        I select criteria index in row  1  Expiration date
    And I check date criteria operators  1
        I select criteria index in row  1  Event end date
    And I check date criteria operators  1
        I select criteria index in row  1  Effective date
    And I check date criteria operators  1
        I select criteria index in row  1  Event start date
    And I check date criteria operators  1
        I select criteria index in row  1  Creation date
    And I check date criteria operators  1
        I select criteria index in row  1  Modification date
    And I check date criteria operators  1
        I select criteria index in row  1  Type


*** Keywords ***

I select criteria index in row
  [Arguments]  ${number}  ${label}
  ${criteria_row} =  Convert to String  ${querywidget_selector} .querystring-criteria-wrapper:nth-child(${number})
  Click Element  css=${criteria_row} .querystring-criteria-index .select2-container a
  Press Key  jquery=:focus  ${label}\n

I check date criteria operators
  [Arguments]  ${number}
  I select criteria operator in row  ${number}  Today
  I select criteria operator in row  ${number}  Within last
  Then Appears  ${number}  .querystring-criteria-value-RelativeDateWidget
  I select criteria operator in row  ${number}  Before date
  Then Appears  ${number}  .querystring-criteria-value-DateWidget
  I select criteria operator in row  ${number}  After date
  Then Appears  ${number}  .querystring-criteria-value-DateWidget
  I select criteria operator in row  ${number}  Within next
  Then Appears  ${number}  .querystring-criteria-value-RelativeDateWidget
  I select criteria operator in row  ${number}  Before today
  I select criteria operator in row  ${number}  Between dates
  Then Appears  ${number}  .querystring-criteria-value-DateRangeWidget

I select criteria operator in row
  [Arguments]  ${number}  ${label}
  ${criteria_selector} =  Convert to String  ${querywidget_selector} .querystring-criteria-wrapper:nth-child(${number}) .querystring-criteria-operator select
  Select From List By Label  css=${criteria_selector}  ${label}

Appears
  [Arguments]  ${number}  ${selector}
  ${criteria_row} =  Convert to String  ${querywidget_selector} .querystring-criteria-wrapper:nth-child(${number})
  Page should contain Element  css=${criteria_row} .querystring-criteria-value ${selector}

Debug2
  Import Library  DebugLibrary
  Debug
