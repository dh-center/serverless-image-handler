import {ReactElement, useState} from "react";
import {Alert, Upload} from "antd";
import {InboxOutlined} from '@ant-design/icons';

function Uploader(): ReactElement {
  const [imageKey, setImageKey] = useState<string | null>(null);

  return (
    <div>
      <Upload.Dragger
        name="image"
        multiple={false}
        action={process.env.REACT_APP_UPLOAD_ENDPOINT}
        onChange={info => {
          const {status} = info.file;
          if (status === 'done') {
            setImageKey(info.file.response.image_key);
          } else if (status === 'error') {
            setImageKey(null);
          }
        }}
      >
        <p className="ant-upload-drag-icon">
          <InboxOutlined/>
        </p>
        <p className="ant-upload-text">Click or drag image to this area to upload</p>
      </Upload.Dragger>
      {imageKey && <Alert
        message="Image uploaded"
        description={`Your image key is '${imageKey}'`}
        type="success"
        showIcon
      />}
    </div>
  );
}

export default Uploader;
