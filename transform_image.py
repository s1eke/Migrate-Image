import re

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
        raise ValueError(f"Invalid image URL: {image_url}")
    
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
    new_domain = 'registry.ap-southeast-1.aliyuncs.com'
    new_namespace = 'migrate-1'
    new_tag = tag
    
    new_image_url = f"{new_domain}/{new_namespace}/{new_name}:{new_tag}"
    
    return new_image_url
