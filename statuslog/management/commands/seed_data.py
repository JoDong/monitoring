import random
from django.core.management import BaseCommand
from domain.models import UrlModel
from statuslog.models import StatusLog


class Command(BaseCommand):
    model_name = 'StatusLog'
    help = '이 커맨드를 통해 랜덤한 테스트 상태 로그 데이터를 만듭니다.'

    def add_arguments(self, parser):
        parser.add_argument('--total', default=1, type=int, help=f'몇개의 {self.model_name}를 생성 하시겠습니까?')

    def handle(self, *args, **options):
        total = options.get('total')
        urls = UrlModel.objects.all()
        status_code = ['200', '300', '400']

        for i in range(total):
            StatusLog.objects.create(
                url=random.choice(urls),
                status=random.choice(status_code),
                process=random.randrange(20, 70)
            )
        self.stdout.write(self.style.SUCCESS(f'{total} {self.model_name} 생성!'))
