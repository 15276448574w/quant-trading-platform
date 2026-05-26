import React from 'react';
import { Card, Button, Empty } from 'antd';

const Backtests: React.FC = () => {
  return (
    <div>
      <div style={{ marginBottom: '16px' }}>
        <Button type="primary">开始回测</Button>
      </div>
      <Card>
        <Empty description="暂无回测结果" />
      </Card>
    </div>
  );
};

export default Backtests;
