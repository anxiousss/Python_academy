import pandas as pd


def data_change(left_x: int, top_y: int, right_x: int, bottom_y: int) -> pd.DataFrame:
    df = pd.read_csv('data.csv')
    df = df[(df['x'] <= right_x) & (left_x <= df['x']) & (df['y'] <= top_y) & (bottom_y <= df['y'])]
    return df


def main():
    left_x, top_y = map(int, input().split())
    right_x, bottom_y = map(int, input().split())
    print(data_change(left_x, top_y, right_x, bottom_y))


if __name__ == '__main__':
    main()
