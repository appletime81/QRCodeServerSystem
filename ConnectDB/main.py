from query_data import query_data
import os


def main():
    sql = "SELECT * FROM file_path"
    data = query_data(sql)
    os.system(f"\\\\{data[0][3]}\\{data[0][1]}\\{data[0][0]}.{data[0][2]}")


if __name__ == '__main__':
    main()
