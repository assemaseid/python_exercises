import json

with open('data.json') as f:
    data = json.load(f)



def limited_output(my_string, min_characters):
    return my_string[:min_characters].ljust(min_characters)



print("""Interface Status
================================================================================""" "\n"
"DN                                                 Description           Speed    MTU" "\n"
"-------------------------------------------------- --------------------  ------  ------"
)
for item in data['imdata']:
    DN = item['l1PhysIf']['attributes']['dn']
    Description = item['l1PhysIf']['attributes']['descr']
    Speed = item['l1PhysIf']['attributes']['speed']
    MTU = item['l1PhysIf']['attributes']['mtu']

    print("{0} {1} {2} {3}".format(
        limited_output(DN, 51),
        limited_output(Description, 20),
        limited_output(Speed, 8),
        limited_output(MTU, 6)
    ))


