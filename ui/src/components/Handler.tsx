import {ReactElement, useState} from "react";
import {Button, Checkbox, Form, Input, Image} from "antd";
import styled from "styled-components";

const HandleWrapper = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
`

function Handler(): ReactElement {
  const [imageUrl, setImageUrl] = useState<string | null>(null);

  const filters = [
    {
      label: 'Grayscale',
      value: 'grayscale'
    },
    {
      label: 'Flip',
      value: 'flip'
    },
    {
      label: 'Invert',
      value: 'invert'
    },
    {
      label: 'Mirror',
      value: 'mirror'
    },
    {
      label: 'Equalize',
      value: 'equalize'
    }
  ];

  const onFinish = (values: any) => {
    setImageUrl(`${process.env.REACT_APP_HANDLE_ENDPOINT}?key=${values.key}${(values.filters && values.filters.length) ? '&' + values.filters.join('&') : ''}`);
  };

  return (
    <HandleWrapper>
      <Form
        name="handler"
        onFinish={onFinish}
      >
        <Form.Item
          label="Image key"
          name="key"
          rules={[
            {
              required: true,
              message: 'Please input image key!'
            }
          ]}
        >
          <Input/>
        </Form.Item>
        <Form.Item
          label="Filters"
          name="filters"
        >
          <Checkbox.Group options={filters}/>
        </Form.Item>
        <Form.Item>
          <Button
            type="primary"
            htmlType="submit"
          >
            Handle image
          </Button>
        </Form.Item>
      </Form>
      {imageUrl && <Image src={imageUrl} width={200}/>}
    </HandleWrapper>
  );
}

export default Handler;
