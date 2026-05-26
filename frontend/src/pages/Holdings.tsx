import React from 'react';
import { Card, Empty } from 'antd';

const Holdings: React.FC = () => {
  return (
    <Card>
      <Empty description="暂无持仓" />
    </Card>
  );
};

export default Holdings;
