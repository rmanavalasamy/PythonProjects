pip install -r requirements.txt
behave -f allure_behave.formatter:AllureFormatter -o temp/ SeleniumAutomation/features/Search.feature
cd allure-2.9.0/bin
allure generate -c -o ../../Reports/ ../../temp/




