from fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Addition Server")

def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

# Register the function as an MCP tool
mcp.tool()(add)

def main():
    """Entry point for the MCP server"""
    mcp.run()

if __name__ == "__main__":
    main()