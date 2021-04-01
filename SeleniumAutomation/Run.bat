
pip install -r requirements.txt
behave -f allure_behave.formatter:AllureFormatter -o Reports/Source/ features/Search.feature
cd allure-2.9.0/bin
allure generate ../../Reports/Source -c -o ../../Reports/Target/




