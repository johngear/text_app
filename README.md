# Quick Fun Project

Fun project to use OpenAI completions API and Twilio to send motivating text messages. Sort of corny, but a fun little project and took like 90 minutes. 

## CRONTAB scheduled 

This will run on my local computer a few times a day. A small isolated program shouldn't slow things down too much, especially because it is mostly API calls and basically no compute. 

## How to schedule

`crontab -e`

In VIM, you can save edits by:

clicking `esc`
typing `:wq` enter

In VIM, click escape then

`ggVGd` to delete everything

## Random Times I selected
39 9 * * * /opt/anaconda3/bin/python /Users/johngearig/Documents/Github/text_app/main.py

10 14 * * * /opt/anaconda3/bin/python /Users/johngearig/Documents/Github/text_app/main.py

4 4 * * * /opt/anaconda3/bin/python /Users/johngearig/Documents/Github/text_app/main.py

10 11 * * * /opt/anaconda3/bin/python /Users/johngearig/Documents/Github/text_app/main.py
