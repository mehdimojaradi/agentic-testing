import pytest


@pytest.mark.asyncio
async def test_user_directory_via_run_agent(run_agent):
    """Validates the GET /users endpoint records using our AI Agent pipeline."""

    # 1. Establish an active session context for this specific execution
    test_session = run_agent.create_session()

    # --- [WHEN STEP] ---
    # Command the agent to pull down the live user list via the tool
    when_prompt = (
        
    )

    # Consume the stream chunks to let the agent populate its memory logs
    async for chunk in run_agent.run(when_prompt, session=test_session, stream=True):
        pass

    # --- [THEN STEP] ---
    # Force the agent to parse its memory history and declare a clear test status
    then_prompt = (
        
        # "Does a user record exist with name='Leanne Graham' and email='Sincere@april.biz'? "
        # "Your final sentence MUST explicitly contain either 'TEST RESULT: PASSED' or 'TEST RESULT: FAILED'."
    )

    response = await run_agent.run(then_prompt, session=test_session)

    expected_email = "Shanna@melissa.tv"
    
    assert expected_email in response.text, (
        f"Test Failed: Expected email '{expected_email}' not found in agent response. "
        f"Actual response was: {response.text}"
    )
