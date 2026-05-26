import React from 'react';
import { Card, Button, Empty } from 'antd';

const Strategies: React.FC = () => {
  return (
    <div>
      <div style={{ marginBottom: '16px' }}>
        <Button type="primary">新建策略</Button>
      </div>
      <Card>
        <Empty description="暂无策略" />
      </Card>
    </div>
  );
};

export default Strategies;
