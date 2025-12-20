

start=(0,0)
goal=(2,2)
actions=['up','down','right','left']

def move(state,action):
    row , col=state
    
    if action=='up':
        row=max(row-1,0)
    elif action=='down':
        row=min(row+1,2)
    elif action=='right':
        col=min(col+1,2)
    elif action=='left':
        col=max(col-1,0)
    return (row,col)


def run():
    curr_state=start
    total_reward=0
    steps=0
    max_steps=20
    
    while curr_state !=goal:
        import random
        action=random.choice(actions)
        next_state=move(curr_state,action)
        
        
        if next_state==goal:
            reward=10
        else:
            reward=-1
            
        total_reward+=reward
        curr_state=next_state
        steps+=1
                
        print(f"Step {steps}: Moved {action} -> {curr_state}, Reward: {reward}")
    
    print(f"Episode finished in {steps} steps, Total reward: {total_reward}")

# Run one episode
run()
    
        
    
