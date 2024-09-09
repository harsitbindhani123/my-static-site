import os
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django.conf import settings

class Command(BaseCommand):
    help = 'Build static site'

    def handle(self, *args, **kwargs):
        pages = [
            {
                'output': 'index.html',
                'template': 'main/index.html',
                'context': {}
            },
        ]

        output_dir = os.path.join(settings.BASE_DIR, 'static_site')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for page in pages:
            output_path = os.path.join(output_dir, page['output'])
            with open(output_path, 'w') as f:
                html = render_to_string(page['template'], page['context'])
                f.write(html)

        self.stdout.write(self.style.SUCCESS('Static site generated successfully'))
