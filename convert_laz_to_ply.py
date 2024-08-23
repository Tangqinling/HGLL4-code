import json
import subprocess
import time

def convert_laz_to_ply(input_laz, output_ply):
    pipeline = {
        "pipeline": [
            {
                "type": "readers.las",
                "filename": input_laz
            },
            {
                "type": "writers.ply",
                "filename": output_ply
            }
        ]
    }

    with open('pipeline.json', 'w') as f:
        json.dump(pipeline, f)

    start_time = time.time()
    result = subprocess.run(['pdal', 'pipeline', 'pipeline.json'], capture_output=True, text=True)
    end_time = time.time()

    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(f"Conversion completed in {end_time - start_time:.2f} seconds")

# 示例输入和输出文件路径
input_laz = r"C:\Users\wenru\Desktop\NEED\Pwllpriddog Oak-pc-poly\point_cloud.laz"
output_ply = r"C:\Users\wenru\Desktop\NEED\Pwllpriddog Oak-pc-poly\point_cloud.ply"

# 执行转换
convert_laz_to_ply(input_laz, output_ply)
