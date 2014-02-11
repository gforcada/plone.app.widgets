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
        Page should contain Element  css=${querywidget_selector}
    SelectCriteriaIndex  1  Expiration date
    SelectCriteriaOperator  1  Today
    SelectCriteriaOperator  1  Within last
    SelectCriteriaOperator  1  Before date
    SelectCriteriaOperator  1  After date
    SelectCriteriaOperator  1  Within next
    SelectCriteriaOperator  1  Before today
    SelectCriteriaOperator  1  Between dates
    SelectCriteriaOperator  1  After today
    SelectCriteriaIndex  1  Event end date
    SelectCriteriaIndex  1  Effective date
    SelectCriteriaIndex  1  Event start date
    SelectCriteriaIndex  1  Creation date
    SelectCriteriaIndex  1  Modification date
    SelectCriteriaIndex  1  Type
    SelectCriteriaIndex  1  Expiration date



*** Keywords ***

SelectCriteriaIndex
  [Arguments]  ${number}  ${label}
  ${criteria_row} =  Convert to String  ${querywidget_selector} .querystring-criteria-wrapper:nth-child(${number})
  Click Element  css=${criteria_row} .querystring-criteria-index .select2-container a
  Press Key  jquery=:focus  ${label}\n

SelectCriteriaOperator
  [Arguments]  ${number}  ${label}
  ${criteria_selector} =  Convert to String  ${querywidget_selector} .querystring-criteria-wrapper:nth-child(${number}) .querystring-criteria-operator select
  Select From List By Label  css=${criteria_selector}  ${label}

IsAppearing
  [Arguments]  ${number}  ${selector}
  ${criteria_row} =  Convert to String  ${querywidget_selector} .querystring-criteria-wrapper:nth-child(${number})
  Wait until page contains Element  css=${criteria_row} .querystring-criteria-value ${selector}
