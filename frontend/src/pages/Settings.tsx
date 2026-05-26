import React from 'react';
import { Card, Form, Input, Button } from 'antd';

const Settings: React.FC = () => {
  return (
    <Card title="系统设置">
      <Form layout="vertical">
        <Form.Item label="API密钥" name="api_key">
          <Input placeholder="输入API密钥" type="password" />
        </Form.Item>
        <Form.Item label="API秘密" name="api_secret">
          <Input placeholder="输入API秘密" type="password" />
        </Form.Item>
        <Form.Item>
          <Button type="primary">保存设置</Button>
        </Form.Item>
      </Form>
    </Card>
  );
};

export default Settings;
