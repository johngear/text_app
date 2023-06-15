# Quick hacked-together project

Fun project to use OpenAI completions API to send motivating text messages. Sort of corny, but a fun little project to work on.

# CRONTAB scheduled this to run on my local computer a few times a day. A small isolated program shouldn't slow things down too much. 
`crontab -e`

In VIM, you can save edits by:
clicking `esc`
typing `:wq` enter

In VIM, click escape then
`ggVGd` to delete everything

# Scheduled to run some random times throughout the day
39 9 * * * /opt/anaconda3/bin/python /Users/johngearig/Documents/Github/text_app/main.py
10 14 * * * /opt/anaconda3/bin/python /Users/johngearig/Documents/Github/text_app/main.py
4 4 * * * /opt/anaconda3/bin/python /Users/johngearig/Documents/Github/text_app/main.py
10 11 * * * /opt/anaconda3/bin/python /Users/johngearig/Documents/Github/text_app/main.py
