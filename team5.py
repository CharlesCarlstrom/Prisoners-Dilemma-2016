team_name = 'Team 5 (Charles and Shawn)' # Only 10 chars displayed.
strategy_name = 'SWAG'
strategy_description = '''Collude every 3 rounds, if that collude is a loss, collude every 4 rounds, and so on, do this 200 times.'''
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history) < 5:
        return 'b'
    elif len(my_history) % 3:
        for o in range(200):
            score = my_history
            x = 2
            if their_history[-x] == 'bc':
                return 'c'
            elif score == score -500:
                x += 1
    else:
        return 'b'
    
    
    
    #TESTING
    
def test_move(my_history, their_history, my_score, their_score, result):
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__': #When game starts
     
    if test_move(my_history='b',
              their_history='c', 
              my_score=100,
              their_score=-500,
              result='b'):
         print 'Test passed'
    