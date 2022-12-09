import os 
import argparse



parser = argparse.ArgumentParser()
parser.add_argument('-pyv', type=str, required=False, help='python version por example python, python3 or py',default = 'python3')
parser.add_argument('-ip', type=bool, required=False, help='install paquets from requieriments.txt',default = False)

args = parser.parse_args()


def run_setup( python_v:str, ip:bool ) -> None:
    print(
    ''' 
        | |   (_) |            / _|                             
        | |__  _| | _____  ___| |_ ___  _ __ _____   _____ _ __ 
        | '_ \| | |/ / _ \/ __|  _/ _ \| '__/ _ \ \ / / _ \ '__|
        | |_) | |   <  __/\__ \ || (_) | | |  __/\ V /  __/ |   
        |_.__/|_|_|\_\___||___/_| \___/|_|  \___| \_/ \___|_|  


        
    '''
)

    # run etl process
    os.system(f'{python_v} ./src/main.py')

    # run api server
    os.system(f'{python_v} ./api/apiMain.py')

    # run streamlit server 
    os.system('streamlit run ./front/home.py')


if __name__ == '__main__':
   run_setup(args.pyv)