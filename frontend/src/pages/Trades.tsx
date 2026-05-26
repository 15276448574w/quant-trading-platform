import React from 'react';
import { Card, Empty } from 'antd';

const Trades: React.FC = () => {
  return (
    <Card>
      <Empty description="暂无交易记录" />
    </Card>
  );
};

export default Trades;
