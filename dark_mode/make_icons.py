from PIL import Image
import os

# 元のアイコンファイルパス
os.chdir(os.path.dirname(__file__))
original_icon_path = 'icon.png'
# アイコンを保存するディレクトリ
output_dir = 'icons'

# 必要なアイコンサイズ
icon_sizes = [16, 32, 48, 128]

# ディレクトリが存在しない場合は作成
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 元のアイコン画像を読み込む
original_icon = Image.open(original_icon_path)

# 各サイズにリサイズして保存
for size in icon_sizes:
    resized_icon = original_icon.resize((size, size), Image.ANTIALIAS)
    output_path = os.path.join(output_dir, f'icon{size}.png')
    resized_icon.save(output_path)

# 確認のため、生成されたファイルリストを表示
os.listdir(output_dir)
