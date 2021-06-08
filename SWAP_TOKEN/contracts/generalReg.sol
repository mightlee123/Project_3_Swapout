pragma solidity ^0.5.5;


import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

///import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/drafts/Counter.sol";


contract swapOut is ERC721Full {
    using Counters for Counters.Counter;
    constructor() public ERC721Full("swapOut", "SWAP") {}

    struct itemInfo {
        address owner;
        string content;
        uint256 price;
        uint256 date;

    }

    mapping(uint256 => itemInfo) public itemCollection;

    event updatedPrice(uint256 tokenId, uint256 price, string reportURI);

    function registerItem(
        address owner,
        string memory content,
        uint256 price,
        uint256 date,
        string memory tokenURI
    ) public returns (uint256) {
        uint256 tokenId = totalSupply();

        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);

        itemCollection[tokenId] = itemInfo(owner, content, price, date);

        return tokenId;
    }

    function priceAdjustment(
        uint256 tokenId,
        uint256 newPrice,
        string memory reportURI
    ) public returns (uint256) {
        itemCollection[tokenId].price = newPrice;

    emit updatedPrice(tokenId, newPrice, reportURI);

        return itemCollection[tokenId].price;
    }
}