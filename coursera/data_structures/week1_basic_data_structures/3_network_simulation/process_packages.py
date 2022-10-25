# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        # write your code here
        art = request[0]
        while len(self.finish_time) > 0 and self.finish_time[0] <= art:
            self.finish_time.pop(0)

        # print(request[0])
        # print(self.finish_time)

        was_dropped = True
        st = -1
        if len(self.finish_time) < self.size:
            was_dropped = False
            if len(self.finish_time) == 0:
                st = request[0]
            else:
                st = self.finish_time[len(self.finish_time) - 1]
            ft = st + request[1]
            self.finish_time.append(ft)

        # print(request)
        # print(self.finish_time)

        return Response(was_dropped, st)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()

    # files = listdir("tests")
    # files.sort()
    # for i, file in enumerate(files):
    #     if file.endswith(".a"):
    #         with open("tests/" + files[i - 1], "r") as f:
    #             content = f.readlines()
    #             buffer_size, n_requests = map(int, content[0].split())
    #             requests = []
    #             for j in range(n_requests):
    #                 arrived_at, time_to_process = map(int, content[j + 1].split())
    #                 requests.append(Request(arrived_at, time_to_process))
    #
    #         answer_resp = []
    #         with open("tests/" + files[i], "r") as f:
    #             content = f.readlines()
    #             for response in content:
    #                 started_at = int(response)
    #                 answer_resp.append(started_at)
    #
    #         buffer = Buffer(buffer_size)
    #         responses = process_requests(requests, buffer)
    #         rr = []
    #         for response in responses:
    #             if not response.was_dropped:
    #                 rr.append(response.started_at)
    #
    #         # print(i)
    #         # print(buffer_size, requests)
    #         # print(responses)
    #         # print(answer_resp)
    #         for r, answer in zip(responses, answer_resp):
    #             # print("resp", r[1])
    #             # print("answer", answer)
    #             assert int(r[1]) == int(answer)
