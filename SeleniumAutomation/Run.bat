
pip install -r SeleniumAutomation/requirements.txt
behave -f allure_behave.formatter:AllureFormatter -o SeleniumAutomation/Reports/Source/ SeleniumAutomation/features/Search.feature
cd SeleniumAutomation/allure-2.9.0/bin
allure generate ../../Reports/Source -c -o ../../Reports/Target/





