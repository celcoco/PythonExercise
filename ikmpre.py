class CM(object):
    def __enter__(self):
        print "1"
        raise IOError()
        return slef
    def __exit__(self,exec_type,exc_val,exc_tb):
        print "ex"
        return False

c = CM()
with c:
    try:
        print "r2"
        raise ValueError()
    except ValueError:
        print "Exc"