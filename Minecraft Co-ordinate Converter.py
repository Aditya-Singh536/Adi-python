blocks_travel_diff = 8
x_coordinates = input('Enter (x) Co-ordinates:')
z_coordinates = input('Enter (z) Co-ordinates:')

def mine_coor_converter(): 

    ask_user = input('What do you want to convert overworld to neter or vice versa. ("ow to n" for overworld to nether and "n to ow" for vice versa):')

    def ov_world_n():
        #OverWorld to Nether

        print('\"OverWorld to Nether\"\n')

        print('Your (x) Co-ordinate:',x_coordinates/blocks_travel_diff)
        print('Your (z) Co-ordinate:',z_coordinates/blocks_travel_diff)

    def n_ov_world():
        #Nether to OverWorld

        print('\"Nether to OverWorld\"\n')

        print('Your (x) Co-ordinate:',x_coordinates*blocks_travel_diff)
        print('Your (z) Co-ordinate:',z_coordinates*blocks_travel_diff)

    if ask_user.lower() == 'ow to n':
        ov_world_n()
    elif ask_user.lower() == 'n to ow':
        n_ov_world()
    else:
        print('Invalid Input!')

if x_coordinates.isfloat() and z_coordinates.isfloat():
    mine_coor_converter
else:
    print(f'Invalid Input! Please check the x ans z coordinates {x_coordinates} and {z_coordinates}.')
