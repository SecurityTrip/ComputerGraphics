class Parser(object):
    v_arr = []
    f_arr = []
    filename = ""

    def parsing(self, filename):
        file = open(filename, 'r')
        for line in file:
            varr = []
            farr = []

            line = line.split()

            try:
                if line[0] == 'v':
                    tmp = [float(line[1]), float(line[2]), float(line[3])]
                    varr.append(tmp)
                if line[0] == 'f':
                    tmp = [float(line[1].split("/")[0]), float(line[2].split("/")[0]), float(line[3].split("/")[0])]
                    farr.append(tmp)

                self.v_arr = varr
                self.f_arr = farr

            except:
                None

    def __init__(self, filename):
        self.filename = filename
        self.parsing(filename)


