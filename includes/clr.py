class Clr(str):
    __styles = {"normal":"0","bold":"1","italic":"3", "under_line":"4", "2under_line":"21", "gray_select":"7", "line_through":"9"}
    __clrs = {"default":0,"gray":90,"red":91,"green":92,"yellow":93,"blue":94,"purple":95,"cyan":96}
    def __init__(self):
        pass

    @staticmethod
    def brush(s:str, clr="default",type="normal"):
        c = clr.startswith("l") and Clr.__clrs[clr.split("_")[-1]]-60 or Clr.__clrs[clr]
        return f"\033[{Clr.__styles[type]};{c}m{s}\033[00m"
    @staticmethod
    def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
        # Print New Line on Complete
        if iteration == total: 
            print()
