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

@xw.func
def double_sum(x, y):
    return 2 * (x + y)
