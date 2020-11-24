@echo off

echo Installing required packages.

pip install --user -r .\requirements.txt

SET exampleFile=".env.example"
SET newFile=".env."

echo Creating environment configuration file

IF EXIST %newFile% (
  echo Configuration file already exists
) ELSE (
  copy %exampleFile% %newFile%
)
echo Done. Please fill the required field in %newFile%

pause