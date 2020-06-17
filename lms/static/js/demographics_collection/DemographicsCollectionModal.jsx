import React, { useState } from 'react';
import { Modal, Button, InputText } from '@edx/paragon/static';

const DemographicsCollectionModal = () => {
  const open = true;
  return (
    <div>
      <div>Start</div>
      <Modal
        open={open}
        title="Modal title."
        label="Test"
        onClose={()=>{}}
        body={
          <div>
          <p>Enter your e-mail address to receive free cat facts!</p>
          <InputText
            name="e-mail"
            label="E-Mail Address"
          />
          </div>
        }
        // parentSelector={this.props.parentSelector}
        // onClose={this.resetModalWrapperState}
        buttons={[
            <Button buttonType="success">Green button!</Button>
        ]}
      />
      <div>End</div>
    </div>
  )
}

export { DemographicsCollectionModal };
