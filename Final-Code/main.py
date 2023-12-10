from pybricks.tools import hub_menu

program = hub_menu('1', '2', '3', '4', '6', 'm')

if program == '1':
    import Mission_1
elif program == '2':
    import Mission_2
elif program == '3':
    import Mission_3
elif program == '6':
    import Mission_6
elif program == 'm':
    import Misson_13
else: 
    import Mission_4
