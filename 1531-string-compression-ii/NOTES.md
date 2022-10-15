==> All we need to decide that which characters we need to keep and which one to Skip and we  have to skip only K characters
1.  will check if we need to keep this char or skip this and go with min of that when we encounter 1st Occurance of any new char
2.  will add cur char to the string when it is same as last char  , We are not trying skipping it here as this we have already tried while selecting the 1st occurance of this char , No point in adding 1st a out of 'aaa' and skipiing any of 2nd or 3rd in all these scenarios resultent will be 'aa' only .
​
​