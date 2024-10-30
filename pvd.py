'''
Prefabricated Vertical Drain
Pattern and Settlement Time Calculation
Python Code
'''

import numpy as np

class Pvd:
    def __init__(self):
        pass

    def calculate(self):

        print('*'*75 + '\n\t\t\tINPUT SOIL AND PVD DATA   '  +'\n' + '*'*75 )
        
        try:
            # Input validation and error handling
            settlement = float(input("Calculated settlement (cm): "))
            if settlement <= 0:
                raise ValueError("Settlement must be positive.")
            
            settlement_limit = float(input("Allowable settlement (cm): "))
            if settlement_limit <= 0:
                raise ValueError("Allowable settlement must be positive.")
            
            cv = float(input("Consolidation coefficient (cm2 / sn): "))
            if cv <= 0:
                raise ValueError("Consolidation coefficient must be positive.")
            
            hd = float(input("Drainage length (m): "))
            if hd <= 0:
                raise ValueError("Drainage length must be positive.")
            
            th = float(input("Mandrel thickness (cm): "))
            if th <= 0:
                raise ValueError("Mandrel thickness must be positive.")
            
            b = float(input("Mandrel width (cm): "))
            if b <= 0:
                raise ValueError("Mandrel width must be positive.")
            
            s = float(input("PVD spacing (m): "))
            if s <= 0:
                raise ValueError("PVD spacing must be positive.")
            
            t = float(input("Time (month): "))
            if t <= 0:
                raise ValueError("Time must be positive.")
            
            khkv = float(input("Horizontal to vertical permeability ratio (kh/kv): "))
            if khkv <= 0:
                raise ValueError("Horizontal to vertical permeability ratio must be positive.")
            
            '''
            Horizontal to vertical permeability ratio (kh/kv) may vary from 1 to 15.

            For homogeneous deposits 1-1.5
            For sedimentary clays with discontinuity lenses and more permeable material layers 2-4
            For bedded clays and other deposits containing more or less permeable layers 3-15

            Rixner et al. (1986)
                        
            '''
            # Calculations
            Ut = (1 - (settlement_limit / settlement)) * 100
            tv = (cv * t * 30) / (hd ** 2)
            Uv = np.sqrt(4 * tv / np.pi) * 100


            print('*'*75 + '\n\t\t\tMETHOD CHOICE   '  +'\n' + '*'*75 )


            # Choose method
            print("Which method do you want to calculate?:")
            print("1. Hansbo (1979)")
            print("2. Atkinson and Eldred (1981)")
            print("3. Fellenius and Castonguay (1985)")
            print("4. Long and Covo (1994)")
            print("5. Abuel-Naga and Bouazza (1994)")
            choice = input("Choose: ")
            if choice not in ['1', '2', '3', '4', '5']:
                raise ValueError("Invalid method choice.")

            # Calculate equivalent diameter based on chosen method
            if choice == '1':
                dw = 2 * (b + th) / np.pi
            elif choice == '2':
                dw = (b + th) / 2
            elif choice == '3':
                dw = np.sqrt(4 * b * th / np.pi)
            elif choice == '4':
                dw = (0.5 * b) + (0.7 * th)
            else:
                dw = 0.45 * b


            print('*'*75 + '\n\t\t\tPATTERN CHOICE   '  +'\n' + '*'*75 )

            # Choose layout
            print("Layout?:")
            print("1. Square")
            print("2. Triangle")
            layout = input('Choose layout: ')
            if layout not in ['1', '2']:
                raise ValueError("Invalid layout choice.")

            # Calculate diameter of equivalent soil cylinder based on chosen layout
            if layout == '1':
                de = 1.128 * s
            else:
                de = 1.05 * s

            # Radial consolidation coefficient
            ch = khkv * cv

            # Spacing ratio
            n = (de / dw) * 100

            alpha = np.log(n) - 0.75

            # Radial time factor
            Tr = (ch * t * 30) / (de ** 2)

            # Radial consolidation degree 
            Ur = (1 - np.exp(-8 * Tr / alpha)) * 100

            # Total degree of consolidation
            Uzr = (1 - ((1 - (Ur / 100)) * (1 - (Uv / 100)))) * 100

            print('*'*75 + '\n\t\t\tCALCULATION RESULTS   '  +'\n' + '*'*75 )

            # Output results
            print("Design results:")
            print(f"Uzr: {Uzr:.2f}%")
            print(f"Ut: {Ut:.2f}%")
            

            if Uzr >= Ut:
                print("Pattern and time is suitable")
            else:
                print("PVD pattern or time is not enough. Please change them and recalculate.")

        except ValueError as e:
            print(f"Error: {e}")

wick_drain = Pvd ()
result = wick_drain.calculate()
