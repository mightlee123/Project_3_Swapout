pragma solidity ^0.7.0;

contract Escrow {
    
    // VARIABLES
    
    enum State {NOT_INITIATED, AWATING_PAYMENT, AWATING_DELIVERY, COMPLETE }
    
    State public currState;
    
    bool public isBuyerIn;
    bool public isSellerIn;
    
    uint public price;
    
    address public buyer;
    address payable public seller;
    
    struct TransactionStruct
        {                        
            
        address buyer; 
        uint buyer_nounce;                          
        }
    
    // MODIFIERS 
    modifier onlyBuyer() {
        require(msg.sender == buyer, "Only the buyer can call this function");
        _;
    }
    
    modifier escrowNotStarted() {
        require(currState == State.NOT_INITIATED);
        _;
    }
    
    // fUNCTIONS
    
    constructor(address _buyer, address payable _seller, uint _price){
        buyer = _buyer;
        seller = _seller;
        price = _price * (1 ether);
    }
    
    function initContract() escrowNotStarted public {
        if(msg.sender == buyer) {
            isBuyerIn = true;
        }
        if (msg.sender == seller) {
            isSellerIn = true;
            
        }
        if (isBuyerIn && isSellerIn) {
            currState = State.AWATING_PAYMENT;
        } 
            
    }
    
    function deposit() onlyBuyer public payable {
        require(currState == State.AWATING_PAYMENT, "Already paid");
        require(msg.value == price, "Wrong deposit amount");
        currState = State.AWATING_DELIVERY;
    }
        
    function confirmDelivery() onlyBuyer payable public {
        require(currState == State.AWATING_DELIVERY, "Cannot confirm delivery");
        seller.transfer(price);
        currState = State.COMPLETE;
    }
    
    function withdraw() onlyBuyer payable public {
        require(currState == State.AWATING_DELIVERY, "Cannot withdraw at this stage");
        payable(msg.sender).transfer(price);
        currState = State.COMPLETE;
    }


    function safeTransferFrom(address from, address to, uint256 tokenId) public {
        safeTransferFrom(from, to, tokenId);
    }
    
}    
