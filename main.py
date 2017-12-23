import test
import graph_generator as gg
import xlsxwriter
from multiprocessing.dummy import Pool as ThreadPool

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0, 0, "Vertex")
worksheet.write(0, 1, "Floyd")
worksheet.write(0, 2, "Dijkstra")


def gen(ver):
    fl = 0
    di = 0
    for _ in range(30):
        kek = gg.generate(ver, ver)
        fl += test.floyd(kek)
        di += test.dij(kek)

    worksheet.write(ver, 0, ver)
    worksheet.write(ver, 1, fl / 10)
    worksheet.write(ver, 2, di / 10)
    print(ver)


pool = ThreadPool(5)
results = pool.map(gen, range(3, 50))

workbook.close()
