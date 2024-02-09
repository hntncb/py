import fire
class Caculator(object):
    def double(seft, number, a = 3):
        return 2* number +a
    
if __name__ == '__main__':
    fire.Fire(Caculator)