import asyncio
import os
from nicegui import ui
import requests
from transform_image.transform_image import transform_image_url

ui.query('body').style(f'background-color: #f4f4f9')

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
REPO_OWNER = os.environ.get('REPO_OWNER')
REPO_NAME = 'Migrate-Image'
WORKFLOW_ID = 'migrate.yaml'


def trigger_github_workflow(image_input_value):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{
        REPO_NAME}/actions/workflows/{WORKFLOW_ID}/dispatches"

    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
    }

    payload = {
        'ref': 'master',
        'inputs': {
            'image_url': image_input_value,
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 204:
        print(f'Workflow triggered successfully')
    else:
        print(f'Failed to trigger workflow: {
              response.status_code}, {response.text}')


async def handle_submit():
    image_address = image_input.value
    transformed_address = transform_image_url(image_address)
    trigger_github_workflow(image_address)

    result_label.set_text(transformed_address)
    progress_bar.visible = True

    run_progress_bar()
    await asyncio.sleep(20)

    progress_bar.visible = False

    [setattr(obj, 'visible', True)
     for obj in (copy_button, result_label)]

    copy_button.on('click', js_handler=f'''
        () => navigator.clipboard.writeText("{transformed_address}")
    ''')


def update_progress():
    if progress_bar.value < 1:
        progress_bar.value += 0.05
    else:
        timer.deactivate()


def run_progress_bar():
    progress_bar.value = 0
    timer.activate()


with ui.card().classes('fixed-center'):
    ui.label('请输入镜像URL').tailwind('font-bold')

    image_input = ui.input(placeholder='例如：alpine:latest')

    progress_bar = ui.linear_progress(value=0, show_value=False, size="20px")
    timer = ui.timer(interval=1, callback=update_progress, active=False)
    ui.button('提交', on_click=handle_submit)
    result_label = ui.label()
    copy_button = ui.button('复制')
    [setattr(obj, 'visible', False)
     for obj in (progress_bar, copy_button, result_label)]

ui.run()
