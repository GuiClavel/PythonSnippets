

def physics(time,v_0,h_0): 
    g = 9.8
    v = v_0 - g * time        
    h = -g/2 * time**2 + v_0 * time + h_0
    return v,h

print('here some physics for nerds')
var_v0 = input('please enter the v0 value: ')
var_v0=float(var_v0)

var_h0 = input('please now indicate a value for definying h0: ')
var_h0=float(var_h0)

var_time = input('finally we need to populate a value for the time t: ')
var_time=float(var_time)

print(physics(var_time,var_v0,var_h0))