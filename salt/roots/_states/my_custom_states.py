import salt

def hello(name = None, par1 = None, par2 = None):
    print('my_custom_states.hello running...')
    print(par1)
    print(par2)

    # Calling custom module    
    __salt__['my_custom_module.hello'](par1)

    # More about return values: https://docs.saltstack.com/en/latest/ref/states/writing.html
    return {
        'name': name,
        'changes': {},
        'comment': '',
        'result': True
    }