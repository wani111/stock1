@echo off
call conda activate stock_program_env
echo GET_MYSTOCK     RUN.....
call python ./get_mystock.py
echo GET_TODAYSTOCK  RUN.....
call python ./get_todaysstock.py
echo GET_KOSPISTOCK  RUN.....
call python ./get_kospistock.py
echo GET_KOSDAQSTOCK RUN.....
call python ./get_kosdaqstock.py