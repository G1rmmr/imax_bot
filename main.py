# imports
import oppenhimer, time

if __name__ == "__main__":
    # link with CGV
    url = "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013&date="
    date = "20230829"

    # set device
    imax = oppenhimer.Device()
    imax.driver.get(url + date)

    # check imax
    movie_name = "오펜하이머"

    while True:
        check = imax.check_imax(movie_name)

        if check: break
        else:
            time.sleep(1)
            imax.driver.refresh()