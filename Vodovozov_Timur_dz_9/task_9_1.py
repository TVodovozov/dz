import time


class TrafficLight:
    __traffic_light_color = "Светофор"

    def run_traffic_lights(self):
        while True:
            print("Red light")
            time.sleep(7)
            print("Yellow light")
            time.sleep(2)
            print("Green light")
            time.sleep(7)


a = TrafficLight()
a.run_traffic_lights()
