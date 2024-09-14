import re


def read_and_split_file(file_path):
    try:
        # 打开文件并读取第一行
        with open(file_path, 'r', encoding='utf-8') as file:
            first_line = file.readline().strip()

        # 以/分割
        parts = first_line.split('/')

        # 检查分割后的结果是否有且仅有两个部分
        if len(parts) != 2:
            raise ValueError(
                "The line does not contain exactly two parts when split by '/'")

        # 返回两个部分
        return parts[0], parts[1]

    except Exception as e:
        # 捕获所有异常并打印错误信息
        print(f"An error occurred: {e}")
        raise


def transform_image_url(image_url):
    # 去除协议信息
    if image_url.startswith("http://"):
        image_url = image_url[len("http://"):]
    elif image_url.startswith("https://"):
        image_url = image_url[len("https://"):]

    # 解析原始镜像地址
    pattern = r'^(?:(?P<domain>[^/]+)/)?(?:(?P<namespace>[^/]+)/)?(?P<name>[^:/]+):(?P<tag>[^:/]+)$'

    match = re.match(pattern, image_url)

    if not match:
        return f"{image_url} 不是正常镜像URL。"

    parts = match.groupdict()

    domain = parts['domain'] or ''
    namespace = parts['namespace']
    name = parts['name'] or ''
    tag = parts['tag'] or 'latest'

    if domain and not namespace:
        namespace = domain
    if not domain and not namespace:
        new_name = name
    else:
        new_name = f"{namespace}-{name}".strip('-')

    # 构建新的镜像地址
    new_domain, new_namespace = read_and_split_file("./dest.txt")

    new_tag = tag

    new_image_url = f"{new_domain}/{new_namespace}/{new_name}:{new_tag}"

    return new_image_url
