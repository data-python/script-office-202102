import xlwings as xw


@xw.sub  # only required if you want to import it or run it via UDF Server
def main():
    wb = xw.Book.caller()
    wb.sheets[0].range("A1").value = "Hello xlwings!"


@xw.func
def hello(name):
    return "hello {0}".format(name)


if __name__ == "__main__":
    xw.books.active.set_mock_caller()
    main()

@xw.sub 
def double_sum():
    wb = xw.Book.caller()
    x = wb.sheets[0].range("B1").value
    y = wb.sheets[0].range("C1").value
    a = str(2 * (x + y))
    wb.sheets[0].range("A1").value = a
