@ECHO OFF
rem AUTHOR @ DOOMSEC

ECHO.

:ONE
IF EXIST %appdata%\AUNICO\LICENSE.DOOM ^
rem cscript msg.vbs  "LICENSE KEY EXIST "
ECHO.
IF NOT EXIST %appdata%\AUNICO\LICENSE.DOOM ^
cscript msg.vbs "LICENSE KEY NOT EXIST"
ECHO.
rem PAUSE
GOTO THREE


:THREE
findstr "verification model-s1" "%appdata%\AUNICO\LICENSE.DOOM" 
if %errorlevel%==0 ( GOTO FOUR ) ELSE ( GOTO END )
rem PAUSE
GOTO END

:FOUR
ECHO FILE VERIFICATION COMPLETE !
ECHO.
ECHO LAUNCHING APPLICATIONS
C:\Aunico\bin\Hospital-Bill.exe
rem PAUSE 
Exit


:END
rem CLS
rem EXIT
rem ECHO END
rem PAUSE
cscript msg.vbs "PLease Contact Customer Service For Application LICENSE"