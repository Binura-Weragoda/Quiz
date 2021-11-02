print ('Hello ,Welcome to Your Knowledge Test')

ans = input('Are you Ready to face your Knowledge Test (yes/no) : ') 
score = 0 
total_q = 10


if ans.lower() == 'yes' :
    ans = input('1. What is the most venomous Snake in the world ?')
    if ans.lower() == 'inland taipan' :
        score += 10
        print('Correct')
    else:
        print('Incorrect')


    ans = input('2. What is the most biggest animal in the world?')
    if ans.lower() == 'blue whale' or ans.lower() == 'antarctic blue whale' :
        score += 10
        print('Correct')
    else:
        print('Incorrect')


    ans = input('3. What is the most fastest animal in the world ?')
    if ans.lower() == 'cheetah' :
        score += 10
        print('Correct')
    else:
        print('Incorrect')


     
    ans = input('4. What is the biggest country in the world ?')
    if ans.lower() == 'russia' :
        score += 10
        print('Correct')
    else:
        print('Incorrect')


    
     
    ans = input('5. Who is the owner of Microsoft Company ?')
    if ans.lower() == 'william henry gates ' :
        score += 10
        print('Correct')
    else:
        print('Incorrect')



    ans = input('6. Who is the present CEO of Apple company ?')
    if ans.lower() ==  'tim cook' :
        score += 10
        print('Correct')
    else:
        print('Incorrect')



    ans = input('7. Who is the present CEO of google ?')
    if ans.lower() ==  'sundar pichai' :
        score += 10
        print('Correct')
    else:
        print('Incorrect')



    
    ans = input('8. What is the Deepest lake in the world ?')
    if ans.lower() ==  'lake baikal' :
        score += 10
        print('Correct')
    else:
        print('Incorrect')



    ans = input('9. What is the Deepest place in the world ?')
    if ans.lower() ==  'mariana trench' :
        score += 10
        print('Correct')
    else:
        print('Incorrect')


    ans = input('10. who had founded the samsung electronics ?')
    if ans.lower() ==  'lee byung-chul' :
        score += 10
        print('Correct')
    else:
        print('Incorrect')


print('You had finished your exam . Let us see what has been happened ', score/total_q, "questions correct.")
mark = (score/total_q) *10

print("Mark: ", mark)
print('Let us meet in another game , Good Bye')
    
    

    
