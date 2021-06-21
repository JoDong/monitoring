import requests
from django.core.validators import URLValidator

from domain.forms import StatusLogCreateForm
from domain.models import UrlModel


# def proc_check_status():
# def get_status():
def status():
    """
    등록된 도메인의 상태를 확인하는 함수
    """
    url_list = UrlModel.objects.all()
    for domain in url_list:
        url: str = domain.url

        # if URLValidator(url):
        #     print(f'ERROR - 003 URLValidator: {url}')
        #     continue

        try:
            response = requests.get(url)

            print(response)
            runtime_ms = response.elapsed.total_seconds()
            runtime = int(round(runtime_ms * 1000))

            status_code = response.status_code

            status_log_form = StatusLogCreateForm(data={
                'url': domain,
                'status': status_code,
                'process': runtime,
            })
            if status_log_form.is_valid():
                status_log = status_log_form.save()
            else:
                pass

            # statuslog = StatusLog.objects.create(
            #     url=domain,
            #     status=status_code,
            #     process=runtime,
            # )

            print(f'{url} : 응답시간:{runtime}ms, 상태코드: {status_code}, log {status_log.pk}')
        except requests.exceptions.ConnectionError as e:
            print(f'ERROR - 001 ConnectionError: {e}')
            continue
        except Exception as e:
            print(f'ERROR - 000 Exception : {e}')

        # time_all = response.headers['Date']
        # time_at = time_all[12:-4]
        # print(f'{url.url} : 시간:{time_at}, 처리시간:{runtime}ms, 상태 코드: {status_code}')