async def test_user_directory_via_run_agent(run_agent, prompts):
    
    when_prompt = prompts("api_validation.txt")
    then_prompt = prompts("qa.txt")
    
    test_session = run_agent.create_session()

    async for chunk in run_agent.run(when_prompt, session=test_session, stream=True):
        pass
    
    response = await run_agent.run(then_prompt, session=test_session)

    expected_email = "Shanna@melissa.tv"
    
    assert expected_email in response.text, (
        f"Test Failed: Expected email '{expected_email}' not found in agent response. "
        f"Actual response was: {response.text}"
    )
